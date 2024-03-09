import { renderHook, act } from '@testing-library/react-hooks';
import { useCurrentTime } from '../useCurrentTime';


describe('useCurrentTime hook', () => {
    const originalToLocaleTimeString = Date.prototype.toLocaleTimeString;
    beforeAll(() => {
        Date.prototype.toLocaleTimeString = jest.fn(() => '10:00:00');
    });
    afterAll(() => {
        Date.prototype.toLocaleTimeString = originalToLocaleTimeString;
    });

    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('10:00:00');
    });
});
