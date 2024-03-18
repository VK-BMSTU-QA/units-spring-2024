import { useCurrentTime } from "../useCurrentTime";
import { renderHook, act } from '@testing-library/react';

beforeEach(() => {
  jest.useFakeTimers();
});

afterEach(() => {
  jest.useRealTimers();
});


describe("test useCurrentTime function", () => {
    it.each([
       {
        times: 1,
       },
       {
        times: 10,
       },
       {
        times: 100,
       }
      ])('useCurrentTime with $dateMock', ({times}) => {
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(1000 * times);
        });

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
      });
});
