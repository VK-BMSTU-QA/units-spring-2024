import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('test useCurrentTime function', () => {

    it('should return correct time', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date(2020, 1, 1, 4, 20, 0));
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe("04:20:00");
        jest.useRealTimers();
    });
});
