import { act, renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

jest.useFakeTimers();
afterEach(jest.restoreAllMocks);

describe('test use current time function', () => {
    it('should update current time every second', () => {
        const currDate = new Date('2024-09-03T12:00:00.000Z');
        jest.spyOn(global, 'Date').mockImplementation(() => currDate);

        const updateCurrTimeHook = renderHook(() => useCurrentTime());

        const initialTime = updateCurrTimeHook.result.current;
        expect(initialTime).toBe(currDate.toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const updatedDate = new Date('2024-09-03T12:00:01.000Z');
        jest.spyOn(global, 'Date').mockImplementation(() => updatedDate);

        const updatedTime = updateCurrTimeHook.result.current;
        expect(updatedTime).toBe(updatedDate.toLocaleTimeString('ru-RU'));
    });

    it('should clear the interval when component is unmounted', () => {
        const clearIntervalMock = jest.spyOn(global, 'clearInterval');
        const updateCurrTimeHook = renderHook(() => useCurrentTime());

        updateCurrTimeHook.unmount();

        expect(clearIntervalMock).toHaveBeenCalled();
    });
});

afterAll(() => {
    jest.useRealTimers();
});
