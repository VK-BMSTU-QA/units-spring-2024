import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('test useCurrentTime function', () => {
    jest.useFakeTimers();

    it('should return the current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });
});