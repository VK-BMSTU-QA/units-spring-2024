import { useCurrentTime } from './useCurrentTime';
import { renderHook, act } from '@testing-library/react';

describe('useCurrentTime', () => {
  jest.useFakeTimers().setSystemTime(new Date('2024-01-01 00:00:00'));
  
  it('returns the current time in true format', () => {
    const { result, unmount } = renderHook(() => useCurrentTime());
    expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);

    unmount();
  });

  it('returns the current time', () => {
    const { result } = renderHook(() => useCurrentTime());

    act(() => {
      jest.advanceTimersByTime(1000 * 10);
    });
    expect(result.current).toBe('00:00:10');
  });

});