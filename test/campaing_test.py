import pytest

from sd_bot.rpgrules.campaign import Campaign
from sd_bot.rpgrules.note import Note

class TestCampaign:
    def test_campaign_name(self):
        campaign = Campaign()
        name = "NAME"
        campaign.set_name(name)
        assert campaign.get_name() == name

    def test_empty_campaign_name(self):
        with pytest.raises(ValueError) as excinfo:
            campaign = Campaign()
            name = ""
            campaign.set_name(name)
        assert "Campaign name cannot be Empty" in str(excinfo.value)

    def test_campaing_master(self):
        campaign = Campaign()
        master = "MASTER"
        campaign.set_master(master)
        assert campaign.get_master() == master

    def test_empty_campaign_master(self):
        with pytest.raises(ValueError) as excinfo:
            campaign = Campaign()
            master = ""
            campaign.set_master(master)
        assert "Campaign master cannot be Empty" in str(excinfo.value)

    def test_zoombie_clock_interval(self):
        campaign = Campaign()
        zoombie_clock_minutes = 10
        campaign.set_zoombie_clock_interval(zoombie_clock_minutes)
        assert campaign.get_zoombie_clock_interval() == zoombie_clock_minutes

    def test_zoombie_clock_min_value(self):
        with pytest.raises(ValueError) as excinfo:
            campaign = Campaign()
            zoombie_clock_minutes = 9
            campaign.set_zoombie_clock_interval(zoombie_clock_minutes)
        assert "Zoombie Clock interval needs to be greater than 10" in str(excinfo.value)

    def test_zombie_clock(self):
        campaign = Campaign()
        campaign.set_zoombie_clock()
        assert campaign.get_zoombie_clock() == 0

    def test_zombie_greater_equal_0(self):
        with pytest.raises(ValueError) as excinfo:
            campaign = Campaign()
            campaign.set_zoombie_clock(-1)
        assert "Zoombie Clock needs to be greater or equal 0" in str(excinfo.value)

    def test_zombie_clock_increment(self):
        campaign = Campaign()
        init_clock = 2
        campaign.set_zoombie_clock(init_clock)
        campaign.increment_zoombie_clock()
        assert campaign.get_zoombie_clock() == init_clock + 1

    def test_set_notes(self):
        campaign = Campaign()
        notes = [
            Note('user','text1'), 
            Note('user','text2')
        ]
        campaign.set_notes(notes)
        assert campaign.get_notes() == notes

    def test_supplies(self):
        campaign = Campaign()
        supplies = 6
        campaign.set_supplies(supplies)
        assert campaign.get_supplies() == supplies

    def test_add_supplies(self):
        campaign = Campaign()
        init_supplies = 6
        supplies = 6
        campaign.set_supplies(init_supplies)
        campaign.add_supplies(supplies)
        assert campaign.get_supplies() == init_supplies + supplies

    def test_remove_supplies(self):
        campaign = Campaign()
        init_supplies = 6
        supplies = 4
        campaign.set_supplies(init_supplies)
        campaign.remove_supplies(supplies)
        assert campaign.get_supplies() == init_supplies - supplies

    def test_min_supplies(self):
        campaign = Campaign()
        init_supplies = 2
        supplies = 4
        campaign.set_supplies(init_supplies)
        campaign.remove_supplies(supplies)
        assert campaign.get_supplies() == 0

    def test_refuge(self):
        campaign = Campaign()
        refuge_level = 3
        campaign.set_refuge(refuge_level)
        assert campaign.get_refuge() == refuge_level

    def test_refuge_greater_equal_0(self):
        with pytest.raises(ValueError) as excinfo:
            campaign = Campaign()
            campaign.set_refuge(-1)
        assert "Refuge Level needs to be greater or equal 0" in str(excinfo.value)

    def test_tick_zoombie_clock(self):
        campaign = Campaign()
        supplies = 4
        refuge_level = 3
        zoombie_clock = 1
        campaign.set_supplies(supplies)
        campaign.set_refuge(refuge_level)
        campaign.set_zoombie_clock(zoombie_clock)
        assert campaign.tick_zoombie_clock() == "Refuge still safe!"
        assert campaign.get_supplies() == supplies - 1
        assert campaign.get_zoombie_clock() == zoombie_clock + 1

    def test_tick_zoombie_clock(self):
        campaign = Campaign()
        supplies = 4
        refuge_level = 3
        zoombie_clock = 2
        campaign.set_supplies(supplies)
        campaign.set_refuge(refuge_level)
        campaign.set_zoombie_clock(zoombie_clock)
        assert campaign.tick_zoombie_clock() == "Refuge invasion!"
        assert campaign.get_supplies() == supplies - 1
        assert campaign.get_zoombie_clock() == 0

    def test_zoombie_clock_empty_sched(self):
        campaign = Campaign()
        assert campaign.queue_clock() == []

    def test_zoombie_clock_sched(self):
        campaign = Campaign()
        supplies = 4
        refuge_level = 3
        zoombie_clock = 2
        zoombie_clock_minutes = 10
        campaign.set_supplies(supplies)
        campaign.set_refuge(refuge_level)
        campaign.set_zoombie_clock(zoombie_clock)        
        campaign.set_zoombie_clock_interval(zoombie_clock_minutes)
        event1 = campaign.start_clock()
        event2 = campaign.start_clock()

        assert event1 not in campaign.queue_clock() 
        assert event2 in campaign.queue_clock() 

    def test_create_campaign(self):
        campaign = Campaign()
        name = "name"
        master = "master"
        zoombie_clock_minutes = 10
        campaign.create_campaign(
            name,
            master,
            zoombie_clock_minutes
        )
        assert campaign.get_name() == name
        assert campaign.get_master() == master
        assert campaign.get_zoombie_clock_interval() == zoombie_clock_minutes
        assert campaign.get_refuge() == 0
        assert campaign.get_supplies() == 0 
        assert campaign.get_zoombie_clock() == 0
