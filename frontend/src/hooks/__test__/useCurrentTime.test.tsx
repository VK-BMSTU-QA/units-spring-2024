import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('test useCurrentTime function', () => {
    jest.useFakeTimers();

    it('should return correct time', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });
});