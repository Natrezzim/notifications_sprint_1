create table notification_messagetag
(
    id         text         not null
        constraint notification_messagetag_pkey
            primary key,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    tag        varchar(255) not null
);

alter table notification_messagetag
    owner to postgres;

create index notification_messagetag_id_9ff02b56_like
    on notification_messagetag (id text_pattern_ops);

create table notification_notification
(
    id          text                     not null
        constraint notification_notification_pkey
            primary key,
    created_at  timestamp with time zone,
    updated_at  timestamp with time zone,
    send_status varchar(50)              not null,
    send_date   timestamp with time zone not null,
    context_id  text                     not null
        constraint notification_notific_context_id_d1d7ec56_fk_notificat
            references notification_notificationcontext
            deferrable initially deferred
);

alter table notification_notification
    owner to postgres;

create index notification_notification_id_d90de4be_like
    on notification_notification (id text_pattern_ops);

create index notification_notification_context_id_d1d7ec56
    on notification_notification (context_id);

create index notification_notification_context_id_d1d7ec56_like
    on notification_notification (context_id text_pattern_ops);

create table notification_notificationcontext
(
    id          text  not null
        constraint notification_notificationcontext_pkey
            primary key,
    params      jsonb not null,
    template_id text  not null
        constraint notification_notific_template_id_a9305185_fk_notificat
            references notification_template
            deferrable initially deferred
);

alter table notification_notificationcontext
    owner to postgres;

create index notification_notificationcontext_id_8ee312b8_like
    on notification_notificationcontext (id text_pattern_ops);

create index notification_notificationcontext_template_id_a9305185
    on notification_notificationcontext (template_id);

create index notification_notificationcontext_template_id_a9305185_like
    on notification_notificationcontext (template_id text_pattern_ops);

create table notification_notificationgroup
(
    id                   text         not null
        constraint notification_notificationgroup_pkey
            primary key,
    created_at           timestamp with time zone,
    updated_at           timestamp with time zone,
    title                varchar(255) not null,
    notification_type_id text         not null
        constraint notification_notific_notification_type_id_4661119d_fk_notificat
            references notification_notificationtype
            deferrable initially deferred
);

alter table notification_notificationgroup
    owner to postgres;

create index notification_notificationgroup_id_fe23f418_like
    on notification_notificationgroup (id text_pattern_ops);

create index notification_notificationgroup_notification_type_id_4661119d
    on notification_notificationgroup (notification_type_id);

create index notification_notificatio_notification_type_id_4661119d_like
    on notification_notificationgroup (notification_type_id text_pattern_ops);


create table notification_notificationgroupuser
(
    id                    bigserial
        constraint notification_notificationgroupuser_pkey
            primary key,
    "user"                uuid not null,
    notification_group_id text not null
        constraint notification_notific_notification_group_i_a60f54f2_fk_notificat
            references notification_notificationgroup
            deferrable initially deferred
);

alter table notification_notificationgroupuser
    owner to postgres;

create index notification_notificationg_notification_group_id_a60f54f2
    on notification_notificationgroupuser (notification_group_id);

create index notification_notificatio_notification_group_id_a60f54f2_like
    on notification_notificationgroupuser (notification_group_id text_pattern_ops);

create table notification_notificationtype
(
    id         text         not null
        constraint notification_notificationtype_pkey
            primary key,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    title      varchar(255) not null
);

alter table notification_notificationtype
    owner to postgres;

create index notification_notificationtype_id_6435165b_like
    on notification_notificationtype (id text_pattern_ops);

create table notification_notificationtypetag
(
    id                   text not null
        constraint notification_notificationtypetag_pkey
            primary key,
    created_at           timestamp with time zone,
    updated_at           timestamp with time zone,
    notification_type_id text not null
        constraint notification_notific_notification_type_id_ee2ff74f_fk_notificat
            references notification_notificationtype
            deferrable initially deferred,
    tag_id               text not null
        constraint notification_notific_tag_id_cd100f75_fk_notificat
            references notification_messagetag
            deferrable initially deferred
);

alter table notification_notificationtypetag
    owner to postgres;

create index notification_notificationtypetag_id_be79e680_like
    on notification_notificationtypetag (id text_pattern_ops);

create index notification_notificationtypetag_notification_type_id_ee2ff74f
    on notification_notificationtypetag (notification_type_id);

create index notification_notificatio_notification_type_id_ee2ff74f_like
    on notification_notificationtypetag (notification_type_id text_pattern_ops);

create index notification_notificationtypetag_tag_id_cd100f75
    on notification_notificationtypetag (tag_id);

create index notification_notificationtypetag_tag_id_cd100f75_like
    on notification_notificationtypetag (tag_id text_pattern_ops);

create table notification_notificationunsubscribeuser
(
    id                   bigserial
        constraint notification_notificationunsubscribeuser_pkey
            primary key,
    "user"               uuid not null,
    notification_type_id text not null
        constraint notification_notific_notification_type_id_a838f5bd_fk_notificat
            references notification_notificationtype
            deferrable initially deferred
);

alter table notification_notificationunsubscribeuser
    owner to postgres;

create index notification_notificationu_notification_type_id_a838f5bd
    on notification_notificationunsubscribeuser (notification_type_id);

create index notification_notificatio_notification_type_id_a838f5bd_like
    on notification_notificationunsubscribeuser (notification_type_id text_pattern_ops);

create table notification_template
(
    id                   text         not null
        constraint notification_template_pkey
            primary key,
    created_at           timestamp with time zone,
    updated_at           timestamp with time zone,
    title                varchar(255) not null,
    subject              varchar(255) not null,
    code                 text         not null,
    notification_type_id text         not null
        constraint notification_templat_notification_type_id_dd6a8d06_fk_notificat
            references notification_notificationtype
            deferrable initially deferred
);

alter table notification_template
    owner to postgres;

create index notification_template_id_009b4cdd_like
    on notification_template (id text_pattern_ops);

create index notification_template_notification_type_id_dd6a8d06
    on notification_template (notification_type_id);

create index notification_template_notification_type_id_dd6a8d06_like
    on notification_template (notification_type_id text_pattern_ops);