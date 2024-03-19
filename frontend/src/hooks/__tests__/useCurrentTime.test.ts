import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime', () => {
    jest.useFakeTimers().setSystemTime(new Date('2024-01-01 12:00:00'));

    it('should update current time every second', () => {
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe('12:00:00');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toBe('12:00:01');
    });
});
