import { redirect } from '@sveltejs/kit';
import ChartService from '../../services/chartService.js';

const service = new ChartService;

export async function load({ locals }) {

    const legislatureAndMeetings = await service.getLegislaturesAndMeetings();
	const latestLegislature = legislatureAndMeetings.slice(-1)[0].legislature;
	const latestMeetingNumber = legislatureAndMeetings.slice(-1)[0].meetings.slice(-1)[0];
    throw redirect(302, `/wortmeldungsverhältnisse/${latestLegislature}/${latestMeetingNumber}`);
}
