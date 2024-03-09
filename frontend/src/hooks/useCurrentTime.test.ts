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
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toStrictEqual(
            new Date().toLocaleTimeString('ru-RU')
        );
    });

    it('cleans up interval on unmount', () => {
        const { unmount } = renderHook(() => useCurrentTime());
        const clearIntervalSpy = jest.spyOn(window, 'clearInterval');

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });
});
