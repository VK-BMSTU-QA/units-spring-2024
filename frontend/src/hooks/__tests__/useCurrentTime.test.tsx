import { useCurrentTime } from "../useCurrentTime";
import { renderHook, act } from "@testing-library/react";


describe('useCurrentTime test', () => {
    jest.useFakeTimers();
    it('should return updated time', () => {
        const date = new Date('23 Feb 2003 10:11:12 GMT');
        jest.setSystemTime(date);
        const {result}  = renderHook(() => useCurrentTime());

        expect(result.current).toBe(date.toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(61000);
        });

        expect(result.current).toBe(new Date('23 Feb 2003 10:12:13 GMT').toLocaleTimeString('ru-RU'));
    });
});