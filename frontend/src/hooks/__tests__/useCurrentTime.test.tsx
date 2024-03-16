import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('test useCurrentTime function', () => {
    jest.useFakeTimers();

    it('should return the current time', () => {
        const expected = new Date().toLocaleTimeString('ru-RU');
        
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(expected);
    });
});
