import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';

jest.useFakeTimers();

function getCurrentTime() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}

describe('useCurrentTime hook tests', () => {
    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(getCurrentTime());
    });

    it('should update current time every second', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(getCurrentTime());

        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).toBe(getCurrentTime());

        act(() => {
            jest.advanceTimersByTime(10000);
        });
        expect(result.current).toBe(getCurrentTime());
    });

    it('should clear interval on unmount', () => {
        const { unmount } = renderHook(() => useCurrentTime());
        const clearIntervalSpy = jest.spyOn(window, 'clearInterval');

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalled();
    });
});
