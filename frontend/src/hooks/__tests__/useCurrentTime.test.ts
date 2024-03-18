import { useCurrentTime } from "../useCurrentTime";
import { renderHook, act } from '@testing-library/react';

beforeEach(() => {
  jest.useFakeTimers().setSystemTime(new Date('2024-03-18 00:00:00'));
});

afterEach(() => {
  jest.useRealTimers();
});


describe("test useCurrentTime function", () => {
    it.each([
       {
        timeSecond: 1,
        expectedTime: '00:00:01',
       },
       {
        timeSecond: 100,
        expectedTime: '00:01:40',
       },
       {
        timeSecond: 3600,
        expectedTime: '01:00:00',
       },
       {
        timeSecond: 24*60*60,
        expectedTime: '00:00:00',
       }
      ])('useCurrentTime with $timeSecond, $expectedTime', ({timeSecond, expectedTime}) => {
        const { result } = renderHook(() => useCurrentTime());
        
        expect(result.current).toBe('00:00:00');

        act(() => {
            jest.advanceTimersByTime(1000 * timeSecond);
        });


        expect(result.current).toBe(expectedTime);
      });
});
