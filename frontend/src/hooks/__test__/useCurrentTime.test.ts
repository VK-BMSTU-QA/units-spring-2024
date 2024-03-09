import { renderHook, act } from '@testing-library/react-hooks';
import { useCurrentTime } from '../useCurrentTime';

describe('test get price function', () => {
    it('should return initial state', () => {
      const currentDate = new Date('2024-08-03T19:03:14.000Z');
      jest.spyOn(global, 'Date').mockImplementation(() => currentDate);

      const updateTimeHook = renderHook(() => useCurrentTime());

      const initialTime = updateTimeHook.result.current;
      expect(initialTime).toBe(currentDate.toLocaleTimeString('ru-RU'));

      act(() => {
          jest.advanceTimersByTime(1000);
      });

      const updatedDate = new Date('2024-08-03T19:03:14.000Z');
      jest.spyOn(global, 'Date').mockImplementation(() => updatedDate);

      const updatedTime = updateTimeHook.result.current;
      expect(updatedTime).toBe(updatedDate.toLocaleTimeString('ru-RU'));
      });
});
