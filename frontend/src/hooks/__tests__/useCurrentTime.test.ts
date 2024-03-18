import { useCurrentTime } from '../useCurrentTime';
import { renderHook, act } from '@testing-library/react';

describe('test useCurrentTime', () => {
    it('returns the current time every second', () => {
        jest.useFakeTimers().setSystemTime(new Date('2024-03-18 00:00:00'));

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe('00:00:00');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toBe('00:00:01');

        act(() => {
            jest.advanceTimersByTime(2000);
        });

        expect(result.current).toBe('00:00:03');

        jest.useRealTimers();
    });
});
