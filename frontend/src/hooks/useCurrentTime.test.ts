import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';

jest.useFakeTimers();

describe('useCurrentTime hook tests', () => {
    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('00:00:00');
    });

    it('should update current time every second', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('00:00:00');

        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).toBe('00:00:01');

        act(() => {
            jest.advanceTimersByTime(10000);
        });
        expect(result.current).toBe('00:00:11');
    });

    it('should clear interval on unmount', () => {
        const { unmount } = renderHook(() => useCurrentTime());
        const clearIntervalSpy = jest.spyOn(window, 'clearInterval');

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalled();
    });
});
