import { renderHook, act } from "@testing-library/react";
import { useCurrentTime } from "./useCurrentTime";


jest.useFakeTimers();

describe('use Current Time tests', () => {
    beforeAll(() => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('01 June 2001 00:00:00').getTime())
      });

    afterAll(() => {
        jest.useRealTimers();
    });

  it('returns the current time', () => {
    const {result} = renderHook(useCurrentTime);

    expect(result.current).toBe('0:00:00');

    act(() => {
        jest.advanceTimersByTime(1000);
      });

    expect(result.current).toBe('0:00:01');
  });
});