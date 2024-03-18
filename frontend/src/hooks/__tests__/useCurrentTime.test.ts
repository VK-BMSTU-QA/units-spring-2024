import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

beforeAll(() => {
  jest.useFakeTimers();
  jest.setSystemTime(new Date("01/01/2000 20:00:00"))
});

afterAll(() => {
  jest.useRealTimers();
});

describe('Use current time test', () => {
  it('should get current time', () => {
      const { result } = renderHook(() => useCurrentTime())
      expect(result.current).
      toStrictEqual("20:00:00");
  });
});
