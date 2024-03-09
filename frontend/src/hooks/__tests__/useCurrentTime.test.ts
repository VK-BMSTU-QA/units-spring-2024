import { renderHook } from "@testing-library/react";
import { useCurrentTime } from "../useCurrentTime";


describe('test use current time function', () => {
    it('should return value with price symbol', () => {
        jest.useFakeTimers()
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'))
        jest.useRealTimers()
    });
})