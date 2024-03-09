import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

const mockDate = new Date('2000-12-31T00:00:00.000Z');

test('use current time hook', () => {
    jest.spyOn(global, 'Date').mockImplementationOnce(() => mockDate);
    const { result } = renderHook(() => useCurrentTime());
    expect(result.current).toStrictEqual(mockDate.toLocaleTimeString('ru-RU'));
});
