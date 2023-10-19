import { redirect } from '@sveltejs/kit';

export async function load({ locals }) {

    const year = new Date().getFullYear();
    throw redirect(302, `/sitzungsverteilung/${year}`);
}
