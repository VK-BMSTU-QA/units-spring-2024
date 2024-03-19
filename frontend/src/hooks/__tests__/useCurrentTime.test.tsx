import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('test use current time hook', () => {

    beforeAll(() => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('20 Mar 2024 12:12:12').getTime())
      });

      afterAll(() => {
        jest.useRealTimers();
      });

    test('should return the current time', () => {
        const { result } = renderHook(() => useCurrentTime());        

        expect(result.current).toBe(`12:12:12`);

        act(() => {
            jest.advanceTimersByTime(10);
        });

        expect(result.current).toBe(`12:12:12`);
    });
});
