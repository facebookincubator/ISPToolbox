import { getCookie } from './utils/Cookie';

interface Event {
    eventType: string;
    sessionId?: string;
    url?: string;
}

class AnalyticsService {
    sessionId: string;

    constructor(sessionId: string) {
        this.sessionId = sessionId;

        window.addEventListener('beforeunload', (_e) => {
            this.trackEvent({ eventType: 'pageview' });
        });
    }

    setSessionId = (sessionId: string) => {
        this.sessionId = sessionId;
    };

    trackEvent = async (event: Event) => {
        event.url = window.location.href;
        if (this.sessionId) {
            event.sessionId = this.sessionId;
        }

        const response = await fetch('/pro/workspace/api/analytics/events/', {
            method: 'POST',
            mode: 'same-origin',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') ?? ''
            },
            body: JSON.stringify(event)
        });
        const res = await response.json();
        return res;
    };
}

export default AnalyticsService;
