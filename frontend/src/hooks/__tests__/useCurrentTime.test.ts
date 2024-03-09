import { renderHook, act } from '@testing-library/react-hooks';
import { useCurrentTime } from '../useCurrentTime';

jest.useFakeTimers();

describe('useCurrentTime', () => {
    it('should update time every second', () => {
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);
        // expect(result.current).not.toBe(result.current);
    });
});

describe('useCurrentTime hook', () => {
    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        const currentTime = result.current;

        expect(currentTime).toEqual(expect.any(String));

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const updatedTime = result.current;
        expect(updatedTime).toEqual(expect.any(String));
        expect(updatedTime).not.toEqual(currentTime);
    });
});
