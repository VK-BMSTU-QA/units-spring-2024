import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

const testDate = "07/03/2024";
const testTime = "20:00:00";

beforeAll(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date(testDate + " " + testTime))
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
            testTime
        );
    });
});
