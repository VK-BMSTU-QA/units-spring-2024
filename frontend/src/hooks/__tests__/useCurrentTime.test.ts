import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

jest.useFakeTimers();

describe('use current time test', () => {
    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        const currentTime = result.current;

        expect(currentTime).toEqual(expect.any(String));

        act(() => {
            jest.advanceTimersByTime(3000);
        });

        const updatedTime = result.current;
        expect(updatedTime).toEqual(expect.any(String));
        expect(updatedTime).not.toEqual(currentTime);
    });
});