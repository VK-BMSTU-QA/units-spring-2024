import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('test UseCurrent hook', () => {
    it('UseCurrent correct date', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });
});
