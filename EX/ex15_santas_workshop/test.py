"""Santa ex tests."""
import pytest
from santa import ChildrenStorage, Child, Gift, GiftStorage


@pytest.fixture()
def children_storage():
    """Children storage."""
    return ChildrenStorage()


def test_child_class__repr():
    """Check Child repr."""
    amanda = Child("Amanda", "England")
    amanda_str = str(amanda)
    exp_str = "Child name: Amanda, Country: England, Type: unknown, Wishlist: []"
    assert amanda_str == exp_str


def test_children_storage__empty_list(children_storage):
    """Check empty list."""
    test_dict = children_storage.all_children
    assert len(test_dict) == 0


def test_children_storage__set_default_gift__empty_wl(children_storage):
    """Children storage. Default gift."""
    amanda = Child("Amanda", "England")
    children_storage.all_children["Amanda"] = amanda
    assert len(children_storage.all_children) == 1
    children_storage.set_default_gift()
    amanda = children_storage.all_children["Amanda"]
    test_list = amanda.wishlist
    assert len(test_list) == 1
    assert test_list[0] == "teddy bear"


def test_children_storage__set_default_gift__wl_dash(children_storage):
    """Children storage. Default gift."""
    children_storage.read_csv_children("short_nice.csv", "nice")
    children_storage.read_wishlist_csv("short_wishlist.csv")
    amanda = children_storage.all_children["Amanda"]
    test_list = amanda.wishlist   # ["-"]
    assert test_list == ["-"]

    children_storage.set_default_gift()
    amanda = children_storage.all_children["Amanda"]
    test_list = amanda.wishlist   # teddy
    assert len(test_list) == 1
    assert test_list[0] == "teddy bear"


def test_children_storage__read_csv_children(children_storage):
    """Children storage. Csv."""
    children_storage.read_csv_children("short_nice.csv", "super")
    test_dict = children_storage.all_children
    assert len(test_dict) == 7
    test_child = children_storage.all_children["Amanda"]
    assert test_child.type == "super"
    assert test_child.country == "Italy"
    assert len(test_child.wishlist) == 0


def test_children_storage__read_wishlist_csv(children_storage):
    """Children storage. Csv."""
    children_storage.read_csv_children("short_naugty.csv", "super")
    children_storage.read_wishlist_csv("short_wishlist.csv")
    test_child = children_storage.all_children["Hollie"]
    assert len(test_child.wishlist) != 0
    assert "Football shoes" in test_child.wishlist


def test_gift_class__repr():
    """Check gift repr."""
    teddy = Gift("Teddy bear", 10, 10, 5)
    teddy_str = str(teddy)
    exp_str = "Gift : Teddy bear, cost: 10, time: 10, weight: 5"
    assert teddy_str == exp_str


@pytest.fixture()
def gift_storage():
    """Gift storage."""
    return GiftStorage()


def test_gift_storage__empty(gift_storage):
    """Test gift storage."""
    test_storage = gift_storage.all_gifts
    assert len(test_storage) == 0


def test_gift_storage__add_gifts(gift_storage):
    """Test gift storage."""
    gift_storage.add_gift("teddy")
    test_storage = gift_storage.all_gifts
    assert len(test_storage) == 1


def test_gift_storage__print_all_gifts(gift_storage):
    """Test gift storage."""
    gift_storage.add_gift("teddy")
    all_gifts_list = gift_storage.print_all_gifts()
    exp_str = "teddy Gift : teddy, cost: 0, time: 0, weight: 0"
    assert all_gifts_list[0] == exp_str


def test_gift_storage__write_to_csv(gift_storage):
    """Test gift storage.Csv."""
    gift_storage.add_gift("teddy")
    filename = "test_db.csv"
    gift_storage.write_to_csv(filename, gift_storage.all_gifts)
    with open(filename, "rt") as csv_file:
        date = csv_file.readlines()
    exp_str_1 = "name,cost,time,weight"
    exp_str_2 = "teddy,0,0,0"
    assert date[0].strip() == exp_str_1
    assert date[1].strip() == exp_str_2


def test_gift_storage__get_info_from_file__gift_present_in_db(gift_storage):
    """Test gift storage.Read from file."""
    gift_name = "Xbox Series X"
    assert len(gift_storage.all_gifts) == 0
    result = gift_storage.get_info_from_file("data_base.csv", gift_name)
    assert result   # True
    assert len(gift_storage.all_gifts) == 1
    xbox = gift_storage.all_gifts[gift_name]
    assert xbox.cost == 399
    assert xbox.time == 60
    assert xbox.weight == 4500


def test_gift_storage__get_info_from_file__gift_in_storage(gift_storage):
    """Test gift storage.Read from file."""
    gift_name = "Xbox Series X"
    gift_storage.add_gift(gift_name)
    assert len(gift_storage.all_gifts) == 1
    result = gift_storage.get_info_from_file("data_base.csv", gift_name)
    assert result  # True
    assert len(gift_storage.all_gifts) == 1
    xbox = gift_storage.all_gifts[gift_name]
    assert xbox.cost == 399
    assert xbox.time == 60
    assert xbox.weight == 4500


def test_gift_storage__get_info_from_file__gift_not_present_in_db(gift_storage):
    """Test gift storage.Read from file"""
    gift_name = "Xbox Series XXX"
    assert len(gift_storage.all_gifts) == 0

    result = gift_storage.get_info_from_file("data_base.csv", gift_name)
    assert result is False

    assert len(gift_storage.all_gifts) == 0


def test_gift_storage__get_info_from_file__gift_not_in_storage(gift_storage):
    """Test gift storage.Read from file"""
    gift_name = "Xbox Series XXX"
    gift_storage.add_gift(gift_name)
    assert len(gift_storage.all_gifts) == 1

    result = gift_storage.get_info_from_file("data_base.csv", gift_name)
    assert result is False

    assert len(gift_storage.all_gifts) == 1


def test_gift_storage__get_info_from_server__gift_not_in_server(gift_storage):
    """Test gift storage.Read from server."""
    gift_name = "Xbox Series XXX"
    gift_storage.get_info_from_server(gift_name)
    assert len(gift_storage.all_gifts) == 1
    xbox = gift_storage.all_gifts[gift_name]
    assert xbox.cost == -1
    assert xbox.time == -1
    assert xbox.weight == -1


def test_gift_storage__get_info_from_server__gift_in_server(gift_storage):
    """Test gift storage.Read from server."""
    gift_name = "Xbox Series X"
    gift_storage.get_info_from_server(gift_name)
    assert len(gift_storage.all_gifts) == 1
    xbox = gift_storage.all_gifts[gift_name]
    assert xbox.cost == 399
    assert xbox.time == 60
    assert xbox.weight == 4500


def test_gift_storage__get_info_from_server__gift_in_db_and_server(gift_storage):
    """Test gift storage.Read from server."""
    gift_name = "Xbox Series X"
    gift_storage.add_gift(gift_name)
    gift_storage.get_info_from_server(gift_name)
    assert len(gift_storage.all_gifts) == 1
    xbox = gift_storage.all_gifts[gift_name]
    assert xbox.cost == 399
    assert xbox.time == 60
    assert xbox.weight == 4500
