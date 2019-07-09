// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to generate a Glue script from a Directed Acyclic Graph (DAG).
 * 
 * ## Example Usage
 * 
 * ### Generate Python Script
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = pulumi.all([aws_glue_catalog_database_source.name, aws_glue_catalog_table_source.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name]).apply(([aws_glue_catalog_database_sourceName, aws_glue_catalog_table_sourceName, aws_glue_catalog_database_destinationName, aws_glue_catalog_table_destinationName, aws_glue_catalog_database_destinationName1, aws_glue_catalog_table_destinationName1]) => aws.glue.getScript({
 *     dagEdges: [
 *         {
 *             source: "datasource0",
 *             target: "applymapping1",
 *         },
 *         {
 *             source: "applymapping1",
 *             target: "selectfields2",
 *         },
 *         {
 *             source: "selectfields2",
 *             target: "resolvechoice3",
 *         },
 *         {
 *             source: "resolvechoice3",
 *             target: "datasink4",
 *         },
 *     ],
 *     dagNodes: [
 *         {
 *             args: [
 *                 {
 *                     name: "database",
 *                     value: `"${aws_glue_catalog_database_sourceName}"`,
 *                 },
 *                 {
 *                     name: "table_name",
 *                     value: `"${aws_glue_catalog_table_sourceName}"`,
 *                 },
 *             ],
 *             id: "datasource0",
 *             nodeType: "DataSource",
 *         },
 *         {
 *             args: [{
 *                 name: "mapping",
 *                 value: "[(\"column1\", \"string\", \"column1\", \"string\")]",
 *             }],
 *             id: "applymapping1",
 *             nodeType: "ApplyMapping",
 *         },
 *         {
 *             args: [{
 *                 name: "paths",
 *                 value: "[\"column1\"]",
 *             }],
 *             id: "selectfields2",
 *             nodeType: "SelectFields",
 *         },
 *         {
 *             args: [
 *                 {
 *                     name: "choice",
 *                     value: "\"MATCH_CATALOG\"",
 *                 },
 *                 {
 *                     name: "database",
 *                     value: `"${aws_glue_catalog_database_destinationName}"`,
 *                 },
 *                 {
 *                     name: "table_name",
 *                     value: `"${aws_glue_catalog_table_destinationName}"`,
 *                 },
 *             ],
 *             id: "resolvechoice3",
 *             nodeType: "ResolveChoice",
 *         },
 *         {
 *             args: [
 *                 {
 *                     name: "database",
 *                     value: `"${aws_glue_catalog_database_destinationName1}"`,
 *                 },
 *                 {
 *                     name: "table_name",
 *                     value: `"${aws_glue_catalog_table_destinationName1}"`,
 *                 },
 *             ],
 *             id: "datasink4",
 *             nodeType: "DataSink",
 *         },
 *     ],
 *     language: "PYTHON",
 * }));
 * 
 * export const pythonScript = example.pythonScript;
 * ```
 * 
 * ### Generate Scala Code
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = pulumi.all([aws_glue_catalog_database_source.name, aws_glue_catalog_table_source.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name]).apply(([aws_glue_catalog_database_sourceName, aws_glue_catalog_table_sourceName, aws_glue_catalog_database_destinationName, aws_glue_catalog_table_destinationName, aws_glue_catalog_database_destinationName1, aws_glue_catalog_table_destinationName1]) => aws.glue.getScript({
 *     dagEdges: [
 *         {
 *             source: "datasource0",
 *             target: "applymapping1",
 *         },
 *         {
 *             source: "applymapping1",
 *             target: "selectfields2",
 *         },
 *         {
 *             source: "selectfields2",
 *             target: "resolvechoice3",
 *         },
 *         {
 *             source: "resolvechoice3",
 *             target: "datasink4",
 *         },
 *     ],
 *     dagNodes: [
 *         {
 *             args: [
 *                 {
 *                     name: "database",
 *                     value: `"${aws_glue_catalog_database_sourceName}"`,
 *                 },
 *                 {
 *                     name: "table_name",
 *                     value: `"${aws_glue_catalog_table_sourceName}"`,
 *                 },
 *             ],
 *             id: "datasource0",
 *             nodeType: "DataSource",
 *         },
 *         {
 *             args: [{
 *                 name: "mappings",
 *                 value: "[(\"column1\", \"string\", \"column1\", \"string\")]",
 *             }],
 *             id: "applymapping1",
 *             nodeType: "ApplyMapping",
 *         },
 *         {
 *             args: [{
 *                 name: "paths",
 *                 value: "[\"column1\"]",
 *             }],
 *             id: "selectfields2",
 *             nodeType: "SelectFields",
 *         },
 *         {
 *             args: [
 *                 {
 *                     name: "choice",
 *                     value: "\"MATCH_CATALOG\"",
 *                 },
 *                 {
 *                     name: "database",
 *                     value: `"${aws_glue_catalog_database_destinationName}"`,
 *                 },
 *                 {
 *                     name: "table_name",
 *                     value: `"${aws_glue_catalog_table_destinationName}"`,
 *                 },
 *             ],
 *             id: "resolvechoice3",
 *             nodeType: "ResolveChoice",
 *         },
 *         {
 *             args: [
 *                 {
 *                     name: "database",
 *                     value: `"${aws_glue_catalog_database_destinationName1}"`,
 *                 },
 *                 {
 *                     name: "table_name",
 *                     value: `"${aws_glue_catalog_table_destinationName1}"`,
 *                 },
 *             ],
 *             id: "datasink4",
 *             nodeType: "DataSink",
 *         },
 *     ],
 *     language: "SCALA",
 * }));
 * 
 * export const scalaCode = example.scalaCode;
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/glue_script.html.markdown.
 */
export function getScript(args: GetScriptArgs, opts?: pulumi.InvokeOptions): Promise<GetScriptResult> {
    return pulumi.runtime.invoke("aws:glue/getScript:getScript", {
        "dagEdges": args.dagEdges,
        "dagNodes": args.dagNodes,
        "language": args.language,
    }, opts);
}

/**
 * A collection of arguments for invoking getScript.
 */
export interface GetScriptArgs {
    /**
     * A list of the edges in the DAG. Defined below.
     */
    readonly dagEdges: { source: string, target: string, targetParameter?: string }[];
    /**
     * A list of the nodes in the DAG. Defined below.
     */
    readonly dagNodes: { args: { name: string, param?: boolean, value: string }[], id: string, lineNumber?: number, nodeType: string }[];
    /**
     * The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
     */
    readonly language?: string;
}

/**
 * A collection of values returned by getScript.
 */
export interface GetScriptResult {
    readonly dagEdges: { source: string, target: string, targetParameter?: string }[];
    readonly dagNodes: { args: { name: string, param?: boolean, value: string }[], id: string, lineNumber?: number, nodeType: string }[];
    readonly language?: string;
    /**
     * The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
     */
    readonly pythonScript: string;
    /**
     * The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
     */
    readonly scalaCode: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
