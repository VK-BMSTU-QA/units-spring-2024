import { updateCategories } from "../updateCategories";

describe('test updateCategories', () => {
    it('should return caterory updated on empty array', () => {
        expect(updateCategories([], 'Для дома')).toStrictEqual(['Для дома']);
    });

    it('should delete selected catetegory', () => {
        const result = updateCategories(['Для дома', 'Электроника'], 'Для дома');
        expect(result).not.toContain('Для дома');
        expect(result).toContain('Электроника');
        expect(result.length).toBe(1);
    });

    it('should add category to not empty array', () => {
        const result = updateCategories(['Для дома'], 'Электроника')
        expect(result).toContain('Для дома');
        expect(result).toContain('Электроника');
        expect(result.length).toBe(2);
    });
});
