import { useCurrentTime } from './useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('useCurrentTime', () => {
  jest.useFakeTimers();
  it('returns the current time in true format', () => {
    const { result, unmount } = renderHook(() => useCurrentTime());
    expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);

    unmount();
  });

  it('returns the current time in true locale', () => {
    const { result, unmount } = renderHook(() => useCurrentTime());
    expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));

    unmount();
  });
});