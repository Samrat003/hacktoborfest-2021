/**
 *@NApiVersion 2.1
 *@NScriptType MapReduceScript
 */

define(['N/log', 'N/record', 'N/runtime', 'N/file', 'N/format', 'N/search'], function (log, record, runtime, file, format, search)
{
    function getInputData()
    {
        log.debug({ title: "PCT-BioBag Get Input", details: "In Get Input Function" })
        var salesorderSearchObj = search.create({
            type: "salesorder",
            filters:
                [
                    ["type", "anyof", "SalesOrd"],
                    "AND",
                    ["mainline", "is", "T"]
                ],
            columns:
                [
                    search.createColumn({ name: "internalid", label: "Internal ID" })
                ]
        });
        var searchResultCount = salesorderSearchObj.runPaged().count;
        log.debug("PCT-BioBag", "Sales Order Count : " + searchResultCount);
        var searchResult = salesorderSearchObj.run().getRange({ start: 0, end: searchResultCount });
        var SO_id_array = new Array();
        for (var getid_index = 0; getid_index < searchResultCount; getid_index++)
        {
            var record_id = searchResult[getid_index].id;
            // log.debug({
            //     title: "PCT-Fushi",
            //     details: "Sales Order Record ID : " + record_id
            // })
            // SO_id_array.push(record_id);
        }
        SO_id_array.push(1461);
        log.debug({
            title: "PCT-BioBag",
            details: "Sales Order Array Length : " + SO_id_array.length
        })
        return SO_id_array;
    }

    function map(context)
    {
        log.debug({ title: "PCT-BioBag MAP", details: "In Map Function" })
        try
        {
            var id = context.value;
            log.debug({ title: "PCT-BioBag MAP", details: "Opration Start For Sales Order Id :" + id })
            var SalesOrder_Load = record.load({
                type: "salesorder",
                id: id
            });
            var pairedIntercompanyTransaction = SalesOrder_Load.getValue({
                fieldId: "intercotransaction"
            })
            log.debug({
                title: "PCT-BioBag",
                details: "Inter Company Transaction Internal Id: " + pairedIntercompanyTransaction
            })
            SalesOrder_Load.setText({ fieldId: 'intercotransaction', text: " " });
            // record.delete({
            //     type: "purchaseorder",
            //     id: pairedIntercompanyTransaction
            // })
            // log.debug({ title: "PCT-BioBag", details: "Purchase Order Deleted" })
            SalesOrder_Load.save();
            log.debug({ title: "PCT-BioBag", details: "Record Saved" })

        }
        catch (ex) { log.error({ title: 'map: error', details: ex }); }

    }


    return {
        getInputData: getInputData,
        map: map
    }
});
