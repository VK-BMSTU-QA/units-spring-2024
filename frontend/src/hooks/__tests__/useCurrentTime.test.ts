import { renderHook } from "@testing-library/react";
import { useCurrentTime } from "../useCurrentTime";


describe('test use current time function', () => {
    it('should return current time', () => {
        jest.useFakeTimers();
        const expected = new Date().toLocaleTimeString('ru-RU');
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(expected);
        jest.useRealTimers();
    });
})
