import { useCurrentTime } from './useCurrentTime';
import { renderHook } from '@testing-library/react';

beforeAll(() => {
    jest.useFakeTimers();
});

afterAll(() => {
    jest.useRealTimers();
});

describe('useCurrentTime hook tests', () => {
    it('returns the current time', () => {
        jest.setSystemTime(new Date(2024, 3, 17, 10, 11, 12));
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('10:11:12');
    });

    it('cleans up interval on unmount', () => {
        const { unmount } = renderHook(() => useCurrentTime());
        const clearIntervalSpy = jest.spyOn(window, 'clearInterval');

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });
});
