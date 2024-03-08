import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

beforeAll(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date("07/03/2024 20:00"))
});

afterAll(() => {
    jest.useRealTimers();
});

describe('test use current time function', () => {
    it('should get current time', () => {
        const { result } = renderHook(() => useCurrentTime())
        expect(
            result.current
        ).toStrictEqual(
            new Date().toLocaleTimeString('ru-RU')
        );
    });
});