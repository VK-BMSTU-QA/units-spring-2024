import { renderHook, act } from '@testing-library/react-hooks';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime', () => {
  it('should update time every second', async () => {
    jest.useFakeTimers();
    const { result } = renderHook(() => useCurrentTime());

    const firstTime = result.current;
    act(() => {
      jest.advanceTimersByTime(1000); 
    });

    expect(result.current).not.toBe(firstTime); 

    jest.useRealTimers();
  });
});