import { renderHook } from "@testing-library/react";
import { useCurrentTime } from "../useCurrentTime";


describe('test use current time function', () => {
    it('should return current time', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date(2023, 3, 17, 18, 38, 40));
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('18:38:40');
        jest.useRealTimers();
    });
})
