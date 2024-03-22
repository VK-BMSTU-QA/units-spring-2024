import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('test use current time hook', () => {
    jest.useFakeTimers();
    test('should return the current time', () => {
        const { result } = renderHook(() => useCurrentTime());

        const testDate = new Date()
        const hours = String(testDate.getHours()).length == 2 ? testDate.getHours():`0${testDate.getHours()}`;
        const minutes = String(testDate.getMinutes()).length == 2 ? testDate.getMinutes():`0${testDate.getMinutes()}`;
        const seconds = String(testDate.getSeconds()).length == 2 ? testDate.getSeconds():`0${testDate.getSeconds()}`;

        expect(result.current).toBe(`${hours}:${minutes}:${seconds}`);

        act(() => {
            jest.advanceTimersByTime(10);
        });

        expect(result.current).toBe(`${hours}:${minutes}:${seconds}`);
    });
});