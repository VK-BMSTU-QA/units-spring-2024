import { useCurrentTime } from './useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('useCurrentTime', () => {
  it('returns the current time', () => {
    jest.useFakeTimers();
    const { result, unmount } = renderHook(() => useCurrentTime());

    // Проверяем, что текущее время соответствует ожидаемому формату
    expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);

    // Продвигаем время вперед на 1 секунду и проверяем, что текущее время обновляется
    jest.advanceTimersByTime(1000);
    expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);

    unmount();
  });
});