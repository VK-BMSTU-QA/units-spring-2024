import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('test useCurrentTime function', () => {
    jest.useFakeTimers();

    it('should return the current time', () => {
        jest.setSystemTime(new Date(2024, 3, 17, 0, 0, 0));

        const expected = '00:00:00';
        
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(expected);
    });
});
