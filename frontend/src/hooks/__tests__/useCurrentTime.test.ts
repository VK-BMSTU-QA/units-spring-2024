import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

jest.useFakeTimers();

describe('useCurrentTime', () => {
  it('returns the current time', () => {
    const { result } = renderHook(() => useCurrentTime());

    expect(typeof result.current).toBe('string');
  });

  it('updates the time every second', () => {
    const { result } = renderHook(() => useCurrentTime());
    expect(typeof result.current).toBe('string');
    const enterTime = result.current;
    act(() => {
      jest.advanceTimersByTime(1000);
    });

    expect(typeof result.current).toBe('string');
    expect(result.current).not.toEqual(enterTime);
  });

  it('cleans up interval on unmount', () => {
    const clearIntervalSpy = jest.spyOn(window, 'clearInterval');
    const { unmount } = renderHook(() => useCurrentTime());

    unmount();

    expect(clearIntervalSpy).toHaveBeenCalled();

    clearIntervalSpy.mockRestore();
  });
});
