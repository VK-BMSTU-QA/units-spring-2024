import { renderHook, act } from "@testing-library/react";
import { useCurrentTime } from "./useCurrentTime";


jest.useFakeTimers();

describe('useCurrentTime', () => {
    beforeAll(() => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('12 June 2003 02:12:00').getTime())
      });

    afterAll(() => {
        jest.useRealTimers();
    });
  it('returns the current time', () => {
    const {result} = renderHook(useCurrentTime);

    expect(result.current).toBe('02:12:00');

    act(() => {
        jest.advanceTimersByTime(1000);
      });

    expect(result.current).toBe('02:12:01');
  });
});