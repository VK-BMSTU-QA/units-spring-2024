import { act, renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

jest.useFakeTimers();
afterEach(jest.restoreAllMocks);

describe('test use current time function', () => {
    it('should update current time every second', () => {
        const updateCurrTimeHook = renderHook(() => useCurrentTime());

        const initialTime = updateCurrTimeHook.result.current;
        expect(initialTime).toBe(new Date().toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const updatedTime = updateCurrTimeHook.result.current;
        expect(updatedTime).toBe(new Date().toLocaleTimeString('ru-RU'));
        expect(updatedTime).not.toBe(initialTime);
    });

    it('should clear the interval when component is unmounted', () => {
        const clearIntervalMock = jest.spyOn(global, 'clearInterval');
        const updateCurrTimeHook = renderHook(() => useCurrentTime());

        updateCurrTimeHook.unmount();

        expect(clearIntervalMock).toHaveBeenCalled();
    });
});
