import { updateCategories } from '../updateCategories';

describe('test apply categories function', () => {
    it('should add new category', () => {
        expect(updateCategories(['Электроника', "Одежда"], 'Для дома')).
        toStrictEqual(['Электроника', "Одежда", "Для дома"]);
    });

    it('should delete category', () => {
        expect(updateCategories(['Электроника', "Одежда"], 'Электроника')).
        toStrictEqual(["Одежда"]);
    });

    it('should delete category', () => {
        expect(updateCategories([], 'Электроника')).
        toStrictEqual(["Электроника"]);
    });
});