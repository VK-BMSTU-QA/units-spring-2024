import { useCurrentTime } from "../useCurrentTime";
import { renderHook, act } from "@testing-library/react";


describe('useCurrentTime test', () => {
    jest.useFakeTimers();
    it('should return array of products', () => {
        const date = new Date('12 Dec 2012 12:12:12 GMT');
        jest.setSystemTime(date);

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe(date.toLocaleTimeString('ru-RU'));
        
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        
        expect(result.current).toBe(new Date('12 Dec 2012 12:12:13 GMT').toLocaleTimeString('ru-RU'));
    });
});