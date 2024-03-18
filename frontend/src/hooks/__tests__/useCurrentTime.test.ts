import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';
import { act } from 'react-dom/test-utils';

describe('test UseCurrent hook', () => {
    jest.useFakeTimers();
    it('UseCurrent correct date', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });
});

