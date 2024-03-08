import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

test('should return current time', () => {
    const { result } = renderHook(() => useCurrentTime());

    act(() => {
        result.current;
    });

    expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
});
