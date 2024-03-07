import { Category } from "../../types";
import { updateCategories } from "../updateCategories";

describe('test updateCategories', () => {
    it('empty currentCategories', () => {
        expect(updateCategories([], 'Для дома')).toContain('Для дома');
    });
    it('delele current category', () => {
        expect(updateCategories(['Для дома', 'Электроника'], 'Для дома')).not.toContain('Для дома');
        expect(updateCategories(['Для дома', 'Электроника'], 'Для дома')).toContain('Электроника');
    });
    it('add category', () => {
        expect(updateCategories(['Для дома'], 'Электроника')).toContain('Для дома');
        expect(updateCategories(['Для дома'], 'Электроника')).toContain('Электроника');
    });
});