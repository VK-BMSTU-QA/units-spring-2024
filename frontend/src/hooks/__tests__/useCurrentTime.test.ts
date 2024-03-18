import { useCurrentTime } from '../useCurrentTime';
import { renderHook, act } from '@testing-library/react';

describe('test useCurrentTime', () => {
    it('returns the current time every second', () => {
        jest.useFakeTimers();

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(2000);
        });

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));

        jest.useRealTimers();
    });
});
