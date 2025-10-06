/** @odoo-module **/
import { ListRenderer } from '@web/views/list/list_renderer';
import { patch } from '@web/core/utils/patch';
import { onWillStart } from '@odoo/owl';
import { rpc } from "@web/core/network/rpc";

patch(ListRenderer.prototype, {
    setup() {
        if (super.setup) {
            super.setup();
        }
        onWillStart(async () => {
            await this._loadLogos();
        });
    },

    async _loadLogos() {
        try {
            const model = this.props && this.props.list && (this.props.list.resModel || this.props.list.model);
            if (!model) {
                return;
            }
            const columns = this.props.archInfo && this.props.archInfo.columns ? this.props.archInfo.columns : [];
            const fieldNames = columns
                .map((c) => c && (c.name || c.fieldName))
                .filter((n) => !!n);
            // Fetch logos per field in one go via a json route that accepts multiple fields
            const data = await rpc('/list_column_logo/get_logos', { model, fields: fieldNames });
            const logos = data || {};
            // Attach logo directly to columns so template can render it without DOM patching
            for (const col of columns) {
                const name = col && (col.name || col.fieldName);
                if (name && logos[name]) {
                    col.logo = logos[name];
                }
            }
        } catch (e) {
            // ignore
        }
    },

});


